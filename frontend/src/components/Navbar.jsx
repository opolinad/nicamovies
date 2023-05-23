import React, { useContext } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from '@mui/material';
import { UserLoggedInContext } from '../App';

const Navbar = () => {
  const {isUserLoogedIn, setIsUserLoogedIn} = useContext(UserLoggedInContext);

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
    setIsUserLoogedIn(false);
  }

  return (
    <Box sx={{ flexGrow: 1, marginBottom: '4vh' }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <Link href={`/`} underline="none" sx={{ fontSize: '1.2rem', color: 'white'}}>
                NicaMovies
            </Link>
          </Typography>
          {
            isUserLoogedIn ?
            <Button color="inherit" onClick={logout}>Logout</Button> :
            <Button color="inherit" href='/login'>Login</Button>
          }
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Navbar;