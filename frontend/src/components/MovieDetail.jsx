import React, {useEffect, useState } from 'react';
import { useParams } from 'react-router';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import RatingContainer from './RatingContainer';

const MovieDetail = () => {
  const { movieId } = useParams();
  const [movieInformation, setMovieInformation] = useState({
    movie: {},
    ratings:[]
  });

  useEffect(() => {
    fetch(`http://${process.env.REACT_APP_API_URL}/movie/${movieId}`)
      .then(response => response.json())
      .then(response => {
        setMovieInformation({
          movie: response.movie,
          ratings: response.ratings
        });
      });
  },[]);

  return (
    <>
      <Card sx={{ minWidth: 275, margin: '0.5% 2%' }}>

        <CardContent>

            <Typography sx={{ fontSize: '2rem', fontWeight: 'bolder' }} color="text.primary" gutterBottom>
                {movieInformation.movie.title}
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Release date: { movieInformation.movie.release_date }
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Genre: {movieInformation.movie.genre}
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Plot: {movieInformation.movie.plot}
            </Typography>

        </CardContent>

      </Card>

      {
        movieInformation.ratings.length > 0 &&
        <RatingContainer
        ratings={movieInformation.ratings}
        />
      }
    </>

  );
}

export default MovieDetail;