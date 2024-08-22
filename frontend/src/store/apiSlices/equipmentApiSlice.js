import { apiSlice } from '../api/apiSlice'

export const equipmentApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return result
          ? [{ type: 'Equipment', id: result.id }]
          : [{ type: 'Equipment', id: 'NEW' }];
      },
      query: (payload) => ({
        url: '/equipments',
        method: 'POST',
        credentials: 'include',  // Ensure credentials are sent
        body: {
          category: payload.category,
          manufacturer: payload.manufacturer,
          model: payload.model,
          size: payload.size,
          price_per_hour: payload.pricePerHour,
          description: payload.description,
        },
      }),
    }),
    fetchEquipments: builder.query({
      providesTags: (result) =>
        result
          ? result.map(({ id }) => ({ type: 'Equipment', id }))
          : [{ type: 'Equipment', id: 'LIST' }],
      query: () => ({
        url: '/equipments',
        method: 'GET',
        credentials: 'include',  // Ensure credentials are sent
      }),
    }),
    updateEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return result
          ? [{ type: 'Equipment', id: equipment.id }]
          : [];
      },
      query: (payload) => ({
        url: `/equipments/equipment/${payload.equipmentId}`,
        method: 'PUT',
        credentials: 'include',  // Ensure credentials are sent
        body: {
          new_price_per_hour: payload.newPricePerHour,
          new_description: payload.newDescription,
        },
      }),
    }),
    getEquipment: builder.query({
      query: (equipmentId) => ({
        url: `/equipments/equipment/${equipmentId}`,
        method: 'GET',
        credentials: 'include',  // Ensure credentials are sent
      }),
      providesTags: (result, error, equipmentId) =>
        result
          ? [{ type: 'Equipment', id: equipmentId }]
          : [],
    }),
    deleteEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return result
          ? [{ type: 'Equipment', id: equipment.id }]
          : [{ type: 'Equipment', id: 'DELETED' }];
      },
      query: (equipmentId) => ({
        url: `/equipments/equipment/${equipmentId}`,
        method: 'DELETE',
        credentials: 'include',  // Ensure credentials are sent
      }),
    }),
    signEquipmentAsDamaged: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return result
          ? [{ type: 'Equipment', id: equipment.id }]
          : [];
      },
      query: (equipmentId) => ({
        url: `/equipments/equipment/${equipmentId}/damaged`,
        method: 'GET',
        credentials: 'include',  // Ensure credentials are sent
      }),
    }),
    getSortedEquipment: builder.query({
      query: (payload) => ({
        url: '/equipments/sort',
        method: 'GET',
        params: {
          ...payload,
        },
        credentials: 'include',  // Ensure credentials are sent
      }),
      providesTags: (result) =>
        result
          ? result.map(({ id }) => ({ type: 'Equipment', id }))
          : [{ type: 'Equipment', id: 'SORTED_LIST' }],
    }),
  }),
})

export const {
  useFetchEquipmentsQuery,
  useCreateEquipmentMutation,
  useUpdateEquipmentMutation,
  useGetEquipmentQuery,
  useDeleteEquipmentMutation,
  useSignEquipmentAsDamagedMutation,
  useGetSortedEquipmentQuery,
} = equipmentApiSlice
