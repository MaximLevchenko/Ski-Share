import { useState } from "react"

import g from "../../App.module.css"
import SkeletonBlock from "../../components/Loaders/SkeletonBlock"
import SortableTable from "../../components/SortableTable/SortableTable"
import search from "../../res/icons/search.svg"
import { useFetchEmployeesQuery } from "../../store/apiSlices/employeeApiSlice"
import s from "./Employees.module.css"

const Employees = () => {
  const { data, error, isLoading } = useFetchEmployeesQuery()
  const [searchTerm, setSearchTerm] = useState('')

  const handleSearchTerm = (event) => {
    setSearchTerm(event.target.value)
  }

  let config = [
    {
      label: "Name",
      render: (employee) => employee.name,
      sortValue: (employee) => employee.name,
    },
    {
      label: "Surname",
      render: (employee) => employee.surname,
      sortValue: (employee) => employee.surname,
    },
    {
      label: "Email",
      render: (employee) => employee.email,
      sortValue: (employee) => employee.email,
    },
    {
      label: "Phone",
      render: (employee) => employee.phone,
      sortValue: (employee) => employee.phone,
    },
    {
      label: "Position",
      render: (employee) => employee.position,
      sortValue: (employee) => employee.position,
    },
    {
      label: "Salary",
      render: (employee) => employee.salary,
      sortValue: (employee) => employee.salary,
    },
  ]

  let content

  if (isLoading) {
    content = <SkeletonBlock />
  } else if (error) {
    content = <div>Some error with table</div>
  } else if (data) {
    const newData = data.filter(
      (user) =>
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.surname.toLowerCase().includes(searchTerm.toLowerCase())
    )

    content = <SortableTable data={newData} config={config} keyFn={keyFn} />
  }

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>Employees</div>
      <div className={s.employeesWrapper}>
        <div className={s.inputWrapper}>
          <img src={search} alt='Search' />
          <input type='text' value={searchTerm} placeholder='Search' onChange={handleSearchTerm} />
        </div>
        <div className={s.tableWrapper}>
          {content}
        </div>
      </div>
    </div>
  )
}

const keyFn = (employee) => {
  return employee.id
}

export default Employees
