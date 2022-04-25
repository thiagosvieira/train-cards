import { Home, Assignment } from '@mui/icons-material'
import { Box, List, ListItem, ListItemButton, ListItemIcon, ListItemText } from '@mui/material'

import React from 'react'

const Sidebar = () => {
  return (
    <Box bgcolor="white"
         flex={1} 
         p={2} 
         sx={{ display:{ xs: "none", sm:"block"} }}
    >
    <Box position="fixed">
      <List>
        <ListItem disablePadding>
          <ListItemButton component="a" href="/home">
            <ListItemIcon>
              <Home />
            </ListItemIcon>
            <ListItemText primary="Home" />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton component="a" href="/treinamentos">
            <ListItemIcon>
              <Assignment />
            </ListItemIcon>
            <ListItemText primary="Treinamentos" />
          </ListItemButton>
        </ListItem>
      </List>
    </Box>  
    </Box>
  )
}

export default Sidebar