import { apiSlice } from '../api/apiSlice'


const clientApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createClient: builder.mutation({
      invalidatesTags: (result, error, user) => {
        return [{ type: 'User', id: user.id }];
      },
      query: (payload) => ({
        url: '/clients',
        method: 'POST',
        body: {
          name: payload.name,
          surname: payload.surname,
          email: payload.email,
          phone: payload.phone,
          passport_number: payload.passportNumber,
          address: payload.address,
          birth_date: payload.birthDate,
        },
      }),
    }),
    fetchClients: builder.query({
      providesTags: (result, error, user) => {
        const tags = result.map((item) => {
          return { type: 'User', id: item.id };
        });
        return tags;
      },
      query: () => ({
        url: '/clients',
        method: 'GET',
      }),
    }),
    deleteClient: builder.mutation({
      invalidatesTags: (result, error, user) => {
        return [{ type: 'User', id: user.id }];
      },
      query: (clientId) => ({
        url: `/clients/client/${clientId}`,
        method: 'DELETE',
      }),
    }),
    updateClient: builder.mutation({
      invalidatesTags: (result, error, user) => {
        return [{ type: 'User', id: user.id }];
      },
      query: (payload) => ({
        url: `/clients/client/${payload.id}`,
        method: 'PUT',
        body: {
          new_email: payload.mail,
          new_phone: payload.newPhone,
          new_passport_number: payload.newPassportNumber,
          new_address: payload.newAddress,
        },
      }),
    }),
    fetchClient: builder.query({
      query: (clientId) => ({
        url: `/clients/client/${clientId}`,
        method: 'GET',
      }),
    }),
    sortClients: builder.query({
      query: (params) => ({
        url: '/clients/sort',
        params: {
          ...params,
        },
      }),
    }),
  }),
})

export const {
  useFetchClientsQuery,
  useFetchClientQuery,
  useCreateClientMutation,
  useDeleteClientMutation,
  useUpdateClientMutation,
  useSortClientsQuery,
} = clientApiSlice
