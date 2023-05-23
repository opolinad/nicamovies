import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

const RatingCard = ({ rating, comment }) => {
  return (
    <Card sx={{ minWidth: 275, margin: '0.5% 2%' }}>
        <CardContent>
            <Typography sx={{ fontSize: '2rem', fontWeight: 'bolder' }} color="text.primary" gutterBottom>
                Rating
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Rating: { rating }
            </Typography>
            <Typography sx={{ fontSize: '1.2rem', }} color="text.secondary" gutterBottom>
                Comment: {comment}
            </Typography>

        </CardContent>

    </Card>
  );
}

export default RatingCard;