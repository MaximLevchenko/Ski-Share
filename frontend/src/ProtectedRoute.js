import { useSelector } from 'react-redux'
import { Navigate, Outlet, useLocation } from 'react-router-dom'

import PageWrapper from './pages/PageWrapper/PageWrapper'
import { selectAccessToken } from './store/slices/authSlice'


const ProtectedRoute = () => {
  const accessToken = useSelector(selectAccessToken)
  const location = useLocation()

  return accessToken ? (
    <PageWrapper>
      <Outlet />
    </PageWrapper>
  ) : (
    <Navigate to='/' state={{ from: location }} replace />
  )
}

export default ProtectedRoute
