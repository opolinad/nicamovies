import React, { createContext, useContext, useState } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { Alert } from '@mui/material';
import { decodeToken } from "react-jwt";
import { useNavigate } from 'react-router-dom';
import { UserLoggedInContext } from '../App';


const LogIn = () => {
    const [alert, setAlert] = useState(null);
    const navigate = useNavigate();
    const {setIsUserLoogedIn} = useContext(UserLoggedInContext);

    const handleSubmit = (event) => {
        event.preventDefault();
        setAlert(null);
        const data = new FormData(event.currentTarget);
        const params = {
            email: data.get('email'),
            password: data.get('password'),
        };
        const options = {
            method: 'POST',
            body: JSON.stringify( params )
        };
        fetch(`http://${process.env.REACT_APP_API_URL}/auth/login`, options )
            .then( response => response.json() )
            .then( response => {
                if (response.status) {
                    setAlert({
                        severity: 'success',
                        message: response.message
                    })
                    const myDecodedToken = decodeToken(response.token);
                    localStorage.setItem('email', myDecodedToken.email);
                    localStorage.setItem('token', response.token);
                    setIsUserLoogedIn(true);
                    setTimeout(() => {
                        navigate('/');
                    },2000);
                } else {
                    setAlert({
                        severity: 'error',
                        message: response.message
                    })
                }
                setTimeout(() => {
                    setAlert(null);
                },3000);
            });
    };

    return (
        <>
            {alert && <Alert severity={alert.severity}>{ alert.message }</Alert>}
            <Container component="main" maxWidth="xs">
            <CssBaseline />
            <Box
                sx={{
                marginTop: 8,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                Sign in
                </Typography>
                <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <TextField
                    margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    autoFocus
                />
                <TextField
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="current-password"
                />
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    sx={{ mt: 3, mb: 2 }}
                >
                    Sign In
                </Button>
                <Grid container>
                    <Grid item>
                    <Link href="/signup" variant="body2">
                        {"Don't have an account? Sign Up"}
                    </Link>
                    </Grid>
                </Grid>
                </Box>
            </Box>
            </Container>
        </>

    );
}

export default LogIn;