import { apiSlice } from '../api/apiSlice'

const rentalApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createNewRental: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return result
          ? [{ type: 'Rental', id: result.id }]
          : [{ type: 'Rental', id: 'NEW' }];
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
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: 'Rental', id })),
              { type: 'Rental', id: 'LIST' },
            ]
          : [{ type: 'Rental', id: 'LIST' }],
      query: () => ({
        url: '/rentals',
        method: 'GET',
      }),
    }),
    deleteRental: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return result
          ? [{ type: 'Rental', id: rental.id }]
          : [{ type: 'Rental', id: 'DELETED' }];
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
      providesTags: (result, error, rentalId) =>
        result
          ? [{ type: 'Rental', id: rentalId }]
          : [],
    }),
    closeRental: builder.mutation({
      invalidatesTags: (result, error, rental) => {
        return result
          ? [{ type: 'Rental', id: rental.id }]
          : [];
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
        return result
          ? [{ type: 'Rental', id: rental.id }]
          : [];
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
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: 'Rental', id })),
              { type: 'Rental', id: 'SORTED_LIST' },
            ]
          : [{ type: 'Rental', id: 'SORTED_LIST' }],
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
