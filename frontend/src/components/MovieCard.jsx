import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { Link } from '@mui/material';

const MovieCard = ({ id, title, releaseDate, genre}) => {
  return (
    <Card sx={{ minWidth: 275, margin: '0.5% 2%' }}>
        <CardContent>
            <Typography sx={{ fontSize: '2rem', fontWeight: 'bolder' }} color="text.primary" gutterBottom>
                {title}
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Release date: { releaseDate }
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Genre: {genre}
            </Typography>

        </CardContent>

        <CardActions>
              <Link href={`/movie/${id}`} underline="none" sx={{ fontSize: '1.2rem'}}>
                More details
            </Link>
        </CardActions>

    </Card>
  );
}

export default MovieCard;