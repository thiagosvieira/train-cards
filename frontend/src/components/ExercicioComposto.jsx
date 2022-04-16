import { Card, CardContent, Stack} from '@mui/material'

import { styled } from '@mui/material/styles'
import React from 'react'


const StyledCard = styled(Card)(({ theme }) => ({
    maxWidth:"100%", 
    margin: "5px",
    backgroundColor: "lightcoral"
}));

const ExercicioComposto = ( exercicio, exercicioConjugado ) => {
  return (  
    <Stack direction="column">
      <StyledCard >
        <CardContent>
          <StyledCard >
            <CardContent>
              <p>{exercicio.descricao}</p>
              <p>Set: {exercicio.set}</p>
              <p>Rep: {exercicio.rep}</p>
              <p>Técnica: {exercicio.tecnica}</p> 
            </CardContent>
          </StyledCard>   

          <StyledCard >
            <CardContent>
              <p>{exercicioConjugado.descricao}</p>
              <p>Set: {exercicioConjugado.set}</p>
              <p>Rep: {exercicioConjugado.rep}</p>
              <p>Técnica: {exercicioConjugado.tecnica}</p> 
            </CardContent>
          </StyledCard>
            <p>Intervalo: {exercicioConjugado.intervalo}</p>
        </CardContent>
      </StyledCard>     
    </Stack>
  )
}

export default ExercicioComposto