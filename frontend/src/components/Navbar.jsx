import styled from '@emotion/styled'
import { AppBar, Avatar, Box, Menu, MenuItem, Toolbar, Typography } from '@mui/material'
import {FitnessCenter} from '@mui/icons-material'
import React, { useState } from 'react'

const StyledToolBar = styled(Toolbar)({
  display:"flex",
  justifyContent:"space-between"
})

const UserBox = styled(Box)({
  display:"flex",
  alignItems: "center",
  gap: "15px"
})

const Navbar = () => {
  const[open, setOpen] = useState(false)
  
  return (
    <AppBar position="sticky">
      <StyledToolBar>
        <Typography variant="h6" sx={{ display:{ xs: "none", sm:"block"} }}>Traning Card's</Typography> 
        <FitnessCenter sx={{ display:{ xs: "block", sm:"none"} }}/>
        <UserBox>
          <Typography> Thiago </Typography> 
          <Avatar 
            sx={{ width: 30, height: 30 }} 
            onClick={e=>setOpen(true)}
          /> 
        </UserBox>
      </StyledToolBar>
      <Menu
        id="demo-positioned-menu"
        aria-labelledby="demo-positioned-button"
        open={open}
        onClose={e=>setOpen(false)}
        anchorOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
      >
        <MenuItem >Profile</MenuItem>
        <MenuItem >My account</MenuItem>
        <MenuItem >Logout</MenuItem>
      </Menu>
    </AppBar>
  )
}

export default Navbar