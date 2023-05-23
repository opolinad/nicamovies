import { Card, CardContent, CardHeader } from '@mui/material';
import React, { useEffect, useState } from 'react';
import MovieCard from './MovieCard';

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
                    {
                        moviesInformation?.length &&
                        moviesInformation.map(movie =>
                            <MovieCard
                                key={movie.id}
                                id={movie.id}
                                title={movie.title}
                                releaseDate={movie.release_date}
                                genre={movie.genre}
                            />

                        )
                    }
                </CardContent>
            </Card>
        </>
    );
}

export default MoviesContainer;