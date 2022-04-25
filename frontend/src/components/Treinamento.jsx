import StarRate from '@mui/icons-material/StarRate';
import ShareIcon from '@mui/icons-material/Share';
import StarOutline from '@mui/icons-material/StarOutline'
import { Card, CardActions, CardContent, CardHeader, Checkbox, IconButton} from '@mui/material'
import { styled } from '@mui/material/styles'
import React from 'react'
import Exercicio from './Exercicio';
import ExercicioComposto from './ExercicioComposto';




const StyledCard = styled(Card)(({ theme }) => ({
    maxWidth:"100%",  
    marginBottom: "8px",  
    [theme.breakpoints.up("md")]:{
        maxWidth:"80%",
        margin: "40px"
    }
}));


const Treinamento = ( treinamento ) => {
  return (  
    <StyledCard >
      <CardHeader
        title={treinamento.titulo}
        subheader={"Criado por: " + treinamento.criadoPor + " Objetivo: " }
      /> 
      <CardContent>       
        <StyledCard >
          <CardHeader
            title={treinamento.titulo}
            subheader={"Musculo(s) alvo: " + treinamento.musculos }
          />
          <CardContent>
            <h3>Exercícios</h3>
            <Exercicio />
            <ExercicioComposto />
          </CardContent>
        </StyledCard> 
      </CardContent>
      <CardActions disableSpacing>
        <IconButton aria-label="treino atual">
          <Checkbox icon={<StarOutline />} checkedIcon={<StarRate sx={{color:"gold"}} />} />
        </IconButton>
        <IconButton aria-label="share">
          <ShareIcon />
        </IconButton>
      </CardActions> 
    </StyledCard>       
  )
}

export default Treinamento