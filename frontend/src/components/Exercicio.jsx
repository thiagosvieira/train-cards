import { Card, CardContent, Stack} from '@mui/material'

import { styled } from '@mui/material/styles'
import React from 'react'


const StyledCard = styled(Card)(({ theme }) => ({
    maxWidth:"100%", 
    margin: "5px"
}));


const Exercicio = ( exercicio ) => {
  return (  
    <Stack direction="column">
      <StyledCard >
         <CardContent>
            <p>{exercicio.descricao}</p>
            <p>Set: {exercicio.set}</p>
            <p>Rep: {exercicio.rep}</p>
            <p>Técnica: {exercicio.tecnica}</p>
            <p>Intervalo: {exercicio.intervalo}</p>
        </CardContent>
      </StyledCard>            
    </Stack>
  )
}

export default Exercicio