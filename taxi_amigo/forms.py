from django import forms
from taxi_amigo.models import *
from fcm_django.models import FCMDevice


class BookTaxiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookTaxiForm, self).__init__(*args, **kwargs)
        # Para cambiar el valor de un campo
        self.fields['state'].initial = "Valor de ejemplo"

        # Si ademas estamos editando un objeto propiedad
        if self.instance:
            # Podemos hacer lo que queramos
            valor_propiedad = self.instance.state

    def save(self, *args, **kwargs):
        # Sobrecargar save devuelve el objeto apunto de ser guardado
        book_taxi = super(BookTaxiForm, self).save(*args, **kwargs)

        # Podemos hacer lo que queramos antes de guardarlo
        customer_player_id = book_taxi.customer.player_id
        book_hour = book_taxi.hour

        if book_taxi.driver is None:
            print ("EL TAXISTA NO HA SIDO ASIGNADO")
            print(customer_player_id)
        else:
            if customer_player_id == "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" or customer_player_id == "":
                print ("AQUI ENTRO PORQUE EL VALOR ES POR DEFECTO")
            else:
                driver_player_id = book_taxi.driver.player_id
                print (driver_player_id)
                body = book_taxi.address + book_taxi.reference
                print(body)
                print(book_taxi.service_type)

                device = FCMDevice.objects.all().first()

                device.registration_id = driver_player_id

                #device.send_message("Title", "Message")
                #device.send_message(data={"test": "test"})
                device.send_message(title="New ride request", body=body, badge="1", sound="default",
                                    data={"request": {"type": "reservation", "mainStreet": book_taxi.address,
                                                      "intersection": "", "reference": book_taxi.reference,
                                                      "serviceType": str(book_taxi.service_type),
                                                      "latitude": book_taxi.latitude,
                                                      "longitude": book_taxi.longitude, "orderInfo": "null",
                                                      "destination_address": book_taxi.destination_address,
                                                      "destination_latitude": book_taxi.destination_latitude,
                                                      "destination_longitude": book_taxi.destination_longitude,
                                                      "state": book_taxi.state},
                                          "rideInfo": "null", "clientId": 57,
                                          "pushTokenClient": book_taxi.customer.player_id})
        # Y finalmente lo guardamos
        # book_taxi.save()
        return book_taxi

    def clean(self):
        # Sobrecargar clean devuelve un diccionario con los campos
        cleaned_data = super(BookTaxiForm, self).clean()
        valor_propiedad = cleaned_data.get("state")

        if len(valor_propiedad) < 3:
            # Podemos lanzar una excepcion que aparecera sobre el campo
            raise forms.ValidationError("Debe tener almenos 3 caracteres")

        # Siempre hay que devolver el diccionario
        return cleaned_data

    class Meta:
        model = BookTaxi
        fields = ['date', 'hour', 'address', 'latitude', 'longitude', 'reference', 'destination_address',
                  'destination_latitude', 'destination_longitude', 'state', 'service_type', 'customer', 'driver', ]
