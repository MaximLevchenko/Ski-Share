import { apiSlice } from '../api/apiSlice'


const rentalApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createNewRental: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return [{ type: 'Rental', id: rental.id }];
      },
      query: (payload) => ({
        url: '/rentals',
        method: 'POST',
        body: {
          date_end: payload.dateEnd,
          payment_type: payload.paymentType,
          base_price: payload.basePrice,
          employee_id: payload.employeeId,
          client_id: payload.clientId,
          equipments: payload.equipments,
        },
      }),
    }),
    fetchRentals: builder.query({
      providesTags: (result, error, rental) => {
        const tags = result.map((item) => {
          return { type: 'Rental', id: item.id };
        });
        return tags;
      },
      query: () => ({
        url: '/rentals',
        method: 'GET',
      }),
    }),
    deleteRental: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return [{ type: 'Rental', id: rental.id }];
      },
      query: (rentalId) => ({
        url: `/rentals/rental/${rentalId}`,
        method: 'DELETE',
      }),
    }),
    fetchRental: builder.query({
      query: (rentalId) => ({
        url: `/rentals/rental/${rentalId}`,
        method: 'GET',
      }),
    }),
    closeRental: builder.query({
      invalidatesTags: (result, error, rental) => {
        return [{ type: 'Rental', id: rental.id }];
      },
      query: (payload) => ({
        url: `/rentals/rental/${payload.id}/close`,
        method: 'PUT',
        body: {
          damage_fee: payload.damage_fee,
          late_return_fee: payload.late_return_fee,
        },
      }),
    }),
    changeRentalDescription: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return [{ type: 'Rental', id: rental.id }];
      },
      query: (payload) => ({
        url: `/rentals/rental/${payload.id}/description`,
        method: 'PUT',
        body: {
          new_description: payload.new_description,
        },
      }),
    }),
    sortRentals: builder.query({
      query: (payload) => ({
        url: `/rentals/sort`,
        method: 'GET',
        params: {
          ...payload,
        },
      }),
    }),
  }),
})

export const {
  useCreateNewRentalMutation,
  useFetchRentalsQuery,
  useDeleteRentalMutation,
  useFetchRentalQuery,
  useCloseRentalMutation,
  useChangeRentalDescriptionMutation,
  useSortRentalsQuery,
} = rentalApiSlice
