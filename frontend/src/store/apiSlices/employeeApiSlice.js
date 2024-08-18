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
      providesTags: (result, error, employee) => {
        const tags = result.map((item) => {
          return { type: 'Employee', id: item.id };
        });
        return tags;
      },
      query: () => ({
        url: '/employees',
        method: 'GET',
      }),
    }),
    deleteEmployee: builder.mutation({
      invalidatesTags: (result, error, employee) => {
        return [{ type: 'Employee', id: employee.id }];
      },
      query: (employeeId) => ({
        url: `/employees/employee/${employeeId}`,
        method: 'DELETE',
      }),
    }),
    updateEmployee: builder.mutation({
      invalidatesTags: (result, error, employee) => {
        return [{ type: 'Employee', id: employee.id }];
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
    }),
    sortEmployees: builder.query({
      query: (payload) => ({
        url: `/employees/sort`,
        method: 'GET',
        params: {
          ...payload
        }
      }),
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
