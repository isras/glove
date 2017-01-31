from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from taxi_amigo.models import Customer, Driver, ServiceType, Coupon, CabRide, Delivery, BookTaxi, ValueSettings
from userprofiles.models import User

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, exceptions

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists,
                               get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')

# Get the UserModel
UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})
    is_driver = serializers.BooleanField()
    is_customer = serializers.BooleanField()

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password, is_driver, is_customer):
        user = None
        user_tmp = None

        if username and password and is_driver or is_customer:
            user_tmp = authenticate(username=username, password=password)
            if user_tmp is not None:
                if user_tmp.is_driver == 1 and is_customer == 0:
                    user = authenticate(username=username, password=password)

                if user_tmp.is_customer == 1 and is_driver == 0:
                    user = authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        is_driver = attrs.get('is_driver')
        is_customer = attrs.get('is_customer')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password, is_driver, is_customer)

            # Authentication through either username or email
            else:
                user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = UserModel.objects.get(email__iexact=email).get_username()
                except UserModel.DoesNotExist:
                    pass

            if username:
                user = self._validate_username_email(username, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = UserModel
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'service_type', 'available', 'latitude', 'longitude',
            'player_id', 'phone', 'address', 'mobile_phone',)
        read_only_fields = ('email',)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    is_driver = serializers.BooleanField(required=True, write_only=True)
    is_customer = serializers.BooleanField(required=True, write_only=True)
    player_id = serializers.CharField(required=False, write_only=True)
    phone = serializers.CharField(required=False, write_only=True)
    address = serializers.CharField(required=False, write_only=True)
    mobile_phone = serializers.CharField(required=False, write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'is_driver': self.validated_data.get('is_driver', ''),
            'is_customer': self.validated_data.get('is_customer', ''),
            'player_id': self.validated_data.get('player_id', ''),
            'phone': self.validated_data.get('phone', ''),
            'address': self.validated_data.get('address', ''),
            'mobile_phone': self.validated_data.get('mobile_phone', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.is_driver = self.cleaned_data.get('is_driver')
        user.is_customer = self.cleaned_data.get('is_customer')
        user.player_id = self.cleaned_data.get('player_id')
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.mobile_phone = self.cleaned_data.get('mobile_phone')
        user.save()

        return user


class ValueSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueSettings
        fields = ('id', 'COUPON_VALUE', 'COUPON_NEW_USER_VALUE')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_driver', 'is_customer', 'service_type',
            'available', 'latitude', 'longitude', 'player_id', 'phone', 'address', 'mobile_phone')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'born_date', 'phone', 'home_address', 'work_address', 'app_user')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'latitude', 'longitude', 'available', 'service_type', 'app_user',)


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'service_name', 'rate',)


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'coupon_code', 'date', 'description', 'status', 'expires', 'coupon_value', 'customer', 'driver')


class CabRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabRide
        fields = (
            'id', 'date', 'initial_address', 'final_address', 'career_total', 'state', 'service_type',
            'customer', 'driver')


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = (
            'id', 'name', 'description', 'initial_address', 'initial_latitude', 'initial_longitude',
            'destination_address', 'destination_latitude', 'destination_longitude',
            'date', 'reference', 'delivery_total', 'state', 'customer', 'driver')


class BookTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTaxi
        fields = (
            'id', 'date', 'hour', 'address', 'latitude', 'longitude', 'reference', 'destination_address',
            'destination_latitude', 'destination_longitude', 'state', 'service_type', 'customer', 'driver')
