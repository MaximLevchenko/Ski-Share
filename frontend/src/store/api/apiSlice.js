import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { logout, setCredentials } from '../slices/authSlice'


const baseQueryAuth = fetchBaseQuery({
  baseUrl: '/',
  credentials: 'include',
  prepareHeaders: (headers, { getState }) => {
    const accessToken = getState().auth.accessToken

    if (accessToken) {
      headers.set('Authorization', `Bearer ${accessToken}`)
      headers.set('Access-Control-Allow-Origin', 'Origin' )
    }

    return headers
  },
})

const baseQueryWithRefresh = async (args, api, extraOptions) => {
  let result = await baseQueryAuth(args, api, extraOptions)
  if (result?.error?.status === 401) {
    // sending refresh query
    const refreshResult = await baseQueryAuth('/auth/refresh', api, extraOptions)
    if (refreshResult?.data) {
      const user = api.getState().auth.user
      // store a new access token
      api.dispatch(setCredentials({ accessToken: refreshResult.data.access_token, user }))
      // refetch original request
      result = await baseQueryAuth(args, api, extraOptions)
    } else {
      api.dispatch(logout())
    }
  }

  return result
}

export const apiSlice = createApi({
  baseQuery: baseQueryWithRefresh,
  endpoints: (builder) => ({}),
})
