import { Card, CardContent, CardHeader } from '@mui/material';
import React, { useContext } from 'react';
import RatingCard from './RatingCard';
import { UserLoggedInContext } from '../App';
import RatingForm from './RatingForm';


const RatingContainer = ({ ratings, fetchMovie }) => {
    const { isUserLoogedIn } = useContext(UserLoggedInContext);

    return (
        <>
            <Card sx={{ margin: '0 3vw' }} >
                <CardHeader title='Ratings' />
                {
                    isUserLoogedIn &&
                    <div style={{margin:'auto', width: '50%', textAlign: 'center'}}>
                        <RatingForm userId={1} fetchMovie={ fetchMovie }/>
                    </div>
                }
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
                                ratingId={rating.id}
                                comment={rating.comment}
                                userId={rating.user_id}
                                fetchMovie={ fetchMovie }
                            />

                        )
                    }
                </CardContent>
            </Card>
        </>
    );
}

export default RatingContainer;