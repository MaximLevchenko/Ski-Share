import { createSlice } from '@reduxjs/toolkit'


const authSlice = createSlice({
  name: 'auth',
  initialState: {
    user: null,
    accessToken: null,
  },
  reducers: {
    setCredentials: (state, action) => {
      const { user, accessToken } = action.payload
      state.user = user
      state.accessToken = accessToken
    },
    logout: (state, action) => {
      state.user = null
      state.accessToken = null
    },
    setAccessToken: (state, action) => {
      state.accessToken = action.payload
    }
  },
})

export const { setCredentials, logout } = authSlice.actions
export const authReducer = authSlice.reducer

export const selectActualUser = state => state.auth.user
export const selectAccessToken = state => state.auth.accessToken