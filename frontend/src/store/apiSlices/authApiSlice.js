import { apiSlice } from '../api/apiSlice'


export const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getCurrentEmployee: builder.query({
      query: () => ({
        url: '/auth/current-employee',
        method: 'GET',
      }),
    }),
    login: builder.mutation({
      query: (payload) => ({
        url: '/auth/login',
        method: 'POST',
        body: {
          email: payload.email,
          password: payload.password
        },
      }),
    }),
    logout: builder.query({
      query: () => ({
        url: '/auth/logout',
        method: 'GET',
      }),
    }),
    refresh: builder.query({
      query: () => ({
        url: '/auth/refresh',
        method: 'GET',
      }),
    }),
  }),
})

export const { useLoginMutation, useRefreshMutation } = authApiSlice
