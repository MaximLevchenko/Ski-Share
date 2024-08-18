import { apiSlice } from '../api/apiSlice'


export const equipmentApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return [{ type: 'Equipment', id: equipment.id }];
      },
      query: (payload) => ({
        url: '/equipments',
        method: 'POST',
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
      providesTags: (result, error, equipment) => {
        const tags = result.map((item) => {
          return { type: 'Equipment', id: item.id };
        });
        return tags;
      },
      query: () => ({
        url: '/equipments',
        method: 'GET',
      }),
    }),
    updateEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return [{ type: 'Equipment', id: equipment.id }];
      },
      query: (payload) => ({
        url: `/equipments/equipment/${payload.equipmentId}`,
        method: 'PUT',
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
      }),
    }),
    deleteEquipment: builder.mutation({
      invalidatesTags: (result, error, equipment) => {
        return [{ type: 'Equipment', id: equipment.id }];
      },
      query: (equipmentId) => ({
        url: `/equipments/equipment/$${equipmentId}`,
        method: 'DELETE',
      }),
    }),
    signEquipmentAsDamaged: builder.query({
      invalidatesTags: (result, error, equipment) => {
        return [{ type: 'Equipment', id: equipment.id }];
      },
      query: (equipmentId) => ({
        url: `/equipments/equipment/${equipmentId}/damaged`,
        method: 'GET',
      }),
    }),
    getSortedEquipment: builder.query({
      query: (payload) => ({
        url: '/equipments/sort',
        params: {
          ...payload
        },
      }),
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
