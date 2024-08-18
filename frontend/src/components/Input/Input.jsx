import s from "./Input.module.css"


const Input = (props) => {
  const { errorMessage, valid, ...rest } = props
  const inputClass = valid ? "" : s.invalidInput

  return (
    <>
      <input className={`${s.Input} ${inputClass}`} {...rest} />
      {errorMessage && <span>{errorMessage}</span>}
    </>
  )
}

export default Input
