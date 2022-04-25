import {  Box  } from '@mui/material'
import React from 'react'
import Treinamento from '../../components/Treinamento'

const Home = () => {
  return (
    <Box bgcolor="white" flex={4} p={2}>
      <Treinamento />
    </Box>
  )
}

export default Home