import React, { useEffect } from 'react'
import api from './services/api'

const App: React.FC = () => {
  const getPatients = async () => {
    const response = await api.patients.getPatients();

    console.log('response', response);
  }

  useEffect(() => {
    getPatients();
  }, [])

  return (
    <div>
      sarasa
    </div>
  )
}

export default App
