from django import forms
import requests
import json
from taxi_amigo.models import *
from django.core.exceptions import ValidationError


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
        obj_propiedad = super(BookTaxiForm, self).save(*args, **kwargs)

        # Podemos hacer lo que queramos antes de guardarlo
        valor_propiedad = obj_propiedad.driver

        if obj_propiedad.driver is None:
            print ("EL TAXISTA NO HA SIDO ASIGNADO")
        else:
            print (valor_propiedad)
            header = {"Content-Type": "application/json; charset=utf-8",
                      "Authorization": "Basic NDZjNzA5ZGEtYzE5Mi00ZTAxLWFiODItZTFjODk5N2ZkZjdk"}

            payload = dict(app_id="3a469011-9fde-40aa-bbd9-a25026f29222",
                           include_player_ids=["2b4ac3aa-82a2-40bd-805a-da5931b4e597"],
                           contents={"en": "PRUEBA NOTIFICACION"})

            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

            print(req.status_code, req.reason)

        # Y finalmente lo guardamos
        # obj_propiedad.save()
        return obj_propiedad

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
