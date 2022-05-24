import React from 'react';
import { Heading  } from '@chakra-ui/react'
import LoginForm from '../components/forms/LoginForm';

const Login: React.FC = () => {
  return (
    <div>
      <Heading as="h2" size="2xl">Login</Heading>
      <LoginForm />
    </div>
  );
}

export default Login;
