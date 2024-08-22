import { apiSlice } from '../api/apiSlice'

const employeeApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    createEmployee: builder.mutation({
      invalidatesTags: (result, error, employee) => {
        return [{ type: 'Employee', id: employee.id }];
      },
      query: (payload) => ({
        url: '/employees',
        method: 'POST',
        body: {
          name: payload.name,
          surname: payload.surname,
          email: payload.email,
          password: payload.password,
          phone: payload.phone,
          salary: payload.salary,
          position: payload.position,
        },
      }),
    }),
    fetchEmployees: builder.query({
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: 'Employee', id })),
              { type: 'Employee', id: 'LIST' },
            ]
          : [{ type: 'Employee', id: 'LIST' }],
      query: () => ({
        url: '/employees',
        method: 'GET',
      }),
    }),
    deleteEmployee: builder.mutation({
      invalidatesTags: (result, error, employee) => {
        return [{ type: 'Employee', id: employee?.id }];
      },
      query: (employeeId) => ({
        url: `/employees/employee/${employeeId}`,
        method: 'DELETE',
      }),
    }),
    updateEmployee: builder.mutation({
      invalidatesTags: (result, error, employee) => {
        return [{ type: 'Employee', id: employee?.id }];
      },
      query: (payload) => ({
        url: `/employees/employee/${payload.employeeId}`,
        method: 'PUT',
        body: {
          new_phone: payload.newPhone,
          new_salary: payload.newSalary,
          new_position: payload.newPosition,
        },
      }),
    }),
    fetchEmployee: builder.query({
      query: (employeeId) => ({
        url: `/employees/employee/${employeeId}`,
        method: 'GET',
      }),
      providesTags: (result, error, employeeId) =>
        result
          ? [{ type: 'Employee', id: employeeId }]
          : [],
    }),
    sortEmployees: builder.query({
      query: (payload) => ({
        url: `/employees/sort`,
        method: 'GET',
        params: {
          ...payload
        }
      }),
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: 'Employee', id })),
              { type: 'Employee', id: 'SORTED_LIST' },
            ]
          : [{ type: 'Employee', id: 'SORTED_LIST' }],
    }),
  }),
})

export const {
  useCreateEmployeeMutation,
  useFetchEmployeesQuery,
  useDeleteEmployeeMutation,
  useUpdateEmployeeMutation,
  useFetchEmployeeQuery,
  useSortEmployeesQuery,
} = employeeApiSlice
