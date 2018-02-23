from django.shortcuts import render
from django.views import View
from reservation.models import Reservation
from django.db.models import Q

from .forms import ReservationForm, ParkingSpaceForm


class ReservationView(View):
    def get(self, request):
        reservation = ReservationForm()

        return render(request, 'reservation/index.html', {'form': reservation})

    def post(self, request):
        reservation_form = ReservationForm(data=request.POST)

        if reservation_form.is_valid():
            start_date = reservation_form.cleaned_data['start_date']
            finish_date = reservation_form.cleaned_data['finish_date']
            parking_space_number = reservation_form.cleaned_data['parking_space_number']

            if Reservation.objects.filter(Q(parking_space_number=parking_space_number,
                                            start_date__range=[start_date, finish_date]) |
                                          Q(parking_space_number=parking_space_number,
                                            finish_date__range=[start_date, finish_date])).exists():
                msg = 'Dates overlaps. Try other dates and / or parking space.'
            else:
                msg = 'Reservation taken.'
                reservation_form.save()
                reservation_form = ReservationForm()

            return render(request, 'reservation/index.html', {'message': msg,
                                                              'form': reservation_form})

        return render(request, 'reservation/index.html', {'form': reservation_form})


class ReservationsListView(View):
    def get(self, request):
        parking_space_number = ParkingSpaceForm()

        return render(request, 'reservation/reservations_search.html', {'form': parking_space_number})

    def post(self, request):
        parking_space_number_form = ParkingSpaceForm(data=request.POST)

        if parking_space_number_form.is_valid():
            space_number = parking_space_number_form.cleaned_data['parking_space_number']
            reservations_list = Reservation.objects.filter(parking_space_number=space_number)

            return render(request, 'reservation/reservations_list.html', {'form': ParkingSpaceForm(),
                                                                          'reservations': reservations_list,
                                                                          'space_number': space_number})

        return render(request, 'reservation/reservations_search.html', {'form': parking_space_number_form})
