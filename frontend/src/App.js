import { Route, Routes } from 'react-router-dom'

import g from './App.module.css'
import ProtectedRoute from './ProtectedRoute'
import Clients from './pages/Clients/Clients'
import Employees from './pages/Employees/Employees'
import Equipment from './pages/Equipment/Equipment'
import ErrorRoute from './pages/ErrorRoute/ErrorRoute'
import Login from './pages/Login/Login'
import NewClient from './pages/NewClient/NewClient'
import NewEquipment from './pages/NewEquipment/NewEquipment'
import NewRent from './pages/NewRent/NewRent'
import Profile from './pages/Profile/Profile'
import Rents from './pages/Rents/Rents'


function App() {
  return (
    <div className={g.App}>
      <Routes>
        <Route path='/' element={<Login />} />
        <Route element={<ProtectedRoute />}>
          <Route path='equipment' element={<Equipment />} />
          <Route path='profile' element={<Profile />} />
          <Route path='clients' element={<Clients />} />
          <Route path='employees' element={<Employees />} />
          <Route path='rents' element={<Rents />} />
          <Route path='new-rent' element={<NewRent />} />
          <Route path='new-client' element={<NewClient />} />
          <Route path='new-equipment' element={<NewEquipment />} />
        </Route>
        <Route path='*' element={<ErrorRoute />} />
      </Routes>
    </div>
  )
}

export default App
