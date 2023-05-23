import { Card, CardContent, CardHeader } from '@mui/material';
import React from 'react';
import RatingCard from './RatingCard';

const RatingContainer = ({ ratings }) => {
    return (
        <>
            <Card sx={{ margin: '0 3vw' }} >
                <CardHeader title='Ratings'/>
                <CardContent sx={{
                    display: 'flex',
                    flexDirection: 'row',
                    flexWrap: 'wrap',
                    justifyContent: 'center'
                }}>
                    {
                        ratings?.length > 0 &&
                        ratings.map(rating =>
                            <RatingCard
                                key={rating.id}
                                rating={rating.rating}
                                comment={rating.comment}
                            />

                        )
                    }
                </CardContent>
            </Card>
        </>
    );
}

export default RatingContainer;