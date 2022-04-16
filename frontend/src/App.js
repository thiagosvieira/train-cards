import Sidebar from "./components/Sidebar"
import Navbar from './components/Navbar'
import { Box, Stack } from '@mui/material'
import { AppRoutes } from "./Routes";


function App() {
  return (
    <Box>
      <Navbar/>
      <Stack direction="row" spacing={2} justifyContent="space-between">
        <Sidebar/>
        <AppRoutes />
      </Stack>
    </Box>
  );
}

export default App;
