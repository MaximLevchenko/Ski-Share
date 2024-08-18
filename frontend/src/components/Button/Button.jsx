import classnames from 'classnames'

import s from "./Button.module.css"


const Button = ({ children, outlined, className, ...rest }) => {
  const classNames = classnames(s.Button, className, outlined ? s.outlined : s.filled)

  return (
    <button className={classNames} {...rest}>
      {children}
    </button>
  )
}

export default Button
