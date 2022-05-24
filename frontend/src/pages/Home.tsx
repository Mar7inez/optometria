import React, { useEffect, useState } from 'react';
import { Heading  } from '@chakra-ui/react'
import api from '../services/api';

const Home: React.FC = () => {
  const [patients, setPatients] = useState<any[]>([])
  const [loaded, setLoaded] = useState(false)

  const getPatients = async () => {
    const response = await api.patients.getPatients();
    setPatients(response);
    setLoaded(true)
  }

  useEffect(() => {
    if (!loaded) {
      getPatients()
    }
  }, [])

  return (
    <div>
    <Heading as="h2" size="2xl">Home</Heading>

      {!loaded && <p>Loading...</p>}
      {loaded && <ul>
        {patients.map(patient => (
          <li key={patient.id}>
            {patient.first_name}
          </li>
        ))}
      </ul>}
    </div>
  );
}

export default Home;
