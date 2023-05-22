import { Card, CardContent, CardHeader, IconButton } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { Add } from '@mui/icons-material';


const MoviesContainer = () => {
    const [moviesInformation, setMoviesInformation] = useState([]);

    useEffect(() => {
        fetch(`http://${process.env.REACT_APP_API_URL}/movie/`)
            .then(response => response.json())
            .then(response => {
                setMoviesInformation(response.data.movies);
            });
    }, []);

    return (
        <>
            <Card sx={{ margin: '0 3vw' }} >
                <CardHeader title='Movies'/>
                <CardContent sx={{
                    display: 'flex',
                    flexDirection: 'row',
                    flexWrap: 'wrap',
                    justifyContent: 'center'
                }}>

                </CardContent>
            </Card>

        </>
    );
}

export default MoviesContainer;