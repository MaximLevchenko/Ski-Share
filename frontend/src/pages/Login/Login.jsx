import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { SlArrowRight } from 'react-icons/sl'
import { useDispatch } from 'react-redux'

import g from '../../App.module.css'
import Button from '../../components/Button/Button'
import Input from '../../components/Input/Input'
import blueSnowFlake from '../../res/pics/blueSnowFlake.png'
import cyanSnowFlake from '../../res/pics/cyanSnowFlake.png'
import logo from '../../res/pics/logo.svg'
import wave from '../../res/pics/lowerWave.png'
import pinkSnowFlake from '../../res/pics/pinkSnowFlake.png'
import violetSnowFlake from '../../res/pics/violetSnowFlake.png'
import { useLoginMutation } from '../../store/apiSlices/authApiSlice'
import { setCredentials } from '../../store/slices/authSlice'
import s from './Login.module.css'


const Login = () => {
  const dispatch = useDispatch()
  const [login] = useLoginMutation()
  const navigate = useNavigate()

  const [formValues, setFormValues] = useState({
    email: '',
    password: '',
  })

  const [error, setError] = useState({})

  const inputOnChange = (e) => {
    setFormValues({ ...formValues, [e.target.name]: e.target.value })
  }

  const inputs = [
    {
      id: 0,
      name: 'email',
      type: 'text',
      placeholder: 'Email',
      label: 'Email',
      errorMessage: 'Username must contain 6-20 characters (uppercase, lowercase or numbers)',
      pattern: '^[A-Za-z0-9]{6,20}$',
      required: true,
    },
    {
      id: 1,
      name: 'password',
      type: 'password',
      placeholder: 'Password',
      label: 'Password',
      errorMessage: 'Password must contain 6-20 characters',
      pattern: '^.{6,20}$',
      required: true,
    },
  ]

  const validateForm = () => {
    const errors = {}

    inputs.forEach((input) => {
      if (input.required && !formValues[input.name]) {
        errors[input.name] = `${input.label} is required`
      } else if (input.pattern && !new RegExp(input.pattern).test(formValues[input.name])) {
        errors[input.name] = input.errorMessage
      }
    })

    setError(errors)
    return Object.keys(errors).length === 0
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    try {
      const data = await login({ email: formValues.email, password: formValues.password }).unwrap()
      dispatch(
        setCredentials({
          user: {
            employeeEmail: data.email,
            employeeId: data.id,
            employeeName: data.name,
            employeePhone: data.phone,
            employeePosition: data.position,
            employeeSalary:data.salary,
            employeeSurname: data.surname,
            latestRentals: data.rentals,
          },
          accessToken: data.access_token,
        })
      )
      setFormValues((state) => ({
        ...state,
        email: '',
        password: '',
      }))
      navigate('equipment')
    } catch (err) {
      console.log(err)
    }
    // if (validateForm()) {
    // }
  }

  const renderedInputs = inputs.map((input) => (
    <div key={input.id} className={s.inputWrapper}>
      <Input
        name={input.name}
        placeholder={input.placeholder}
        value={formValues[input.name]}
        type={input.type}
        onChange={inputOnChange}
        errorMessage={error[input.name]}
        valid={!error[input.name]}
      />
    </div>
  ))

  const snowFlakes = [
    { icon: cyanSnowFlake, style: s.cyanSnowFlake, alt: 'CyanSnowFlake' },
    { icon: blueSnowFlake, style: s.blueSnowFlake, alt: 'BlueSnowFlake' },
    { icon: pinkSnowFlake, style: s.pinkSnowFlake, alt: 'PinkSnowFlake' },
    { icon: violetSnowFlake, style: s.violetSnowFlake, alt: 'VioletSnowFlake' },
  ]

  const renderedSnowFlakes = snowFlakes.map((snowFlake) => (
    <div className={snowFlake.style} key={snowFlake.alt}>
      <img src={snowFlake.icon} alt={snowFlake.alt} />
    </div>
  ))

  return (
    <>
      {renderedSnowFlakes}
      <div className={s.Login}>
        <div className={g.container}>
          <div className={s.loginContainer}>
            <div className={s.logoRow}>
              <img src={logo} alt='Ski share logo' />
            </div>
            <div className={s.formWrapper}>
              <form onSubmit={handleSubmit}>
                <div className={s.formTitle}>Hi, friend. Please, log in</div>
                {renderedInputs}
                <div className={s.buttonWrapper}>
                  <Button>
                    Log in
                    <SlArrowRight alt='Arrow right' size={15} />
                  </Button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div className={s.wave}>
        <img src={wave} alt='Wave' />
      </div>
    </>
  )
}

export default Login
