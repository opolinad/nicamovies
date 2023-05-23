import React, { useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { Alert, CardActions, IconButton, Snackbar } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { useParams } from 'react-router-dom';

const RatingCard = ({ rating, comment, userId, fetchMovie, ratingId }) => {
    const loggedUserId = Number(localStorage.getItem('userId'));
    const { movieId } = useParams();
    const [alert, setAlert] = useState(null);
    const [open, setOpen] = useState(false);

    const handleClose = (event = null, reason) => {
        if (reason === 'clickaway') {
          return;
        }
        setOpen(false);
    };

    const deleteRating = () => {
        const params = {
            Authorization: `Bearer ${localStorage.getItem('token')}`
        };
        const options = {
            method: 'DELETE',
            body: JSON.stringify(params),
        };
        fetch(`http://${process.env.REACT_APP_API_URL}/movie/rating/${ratingId}`, options )
            .then( response => response.json() )
            .then( response => {
                if (response.status) {
                    setAlert({
                        severity: 'success',
                        message: response.message
                    });
                    setOpen(true);
                    fetchMovie();
                } else {
                    setAlert({
                        severity: 'error',
                        message: response.message
                    });
                    setOpen(true);
                }
            });
    };

    return (
        <>
            {
                alert &&
                <Snackbar
                    open={open}
                    autoHideDuration={5000}
                    onClose={handleClose}
                    anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
                >
                    <Alert onClose={handleClose} severity={ alert.severity} sx={{ width: '100%' }}>
                        {alert.message}
                    </Alert>
                </Snackbar>
            }
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
                {
                    loggedUserId === userId &&
                    <CardActions>
                        <IconButton aria-label="delete" color="error" onClick={deleteRating}>
                            <DeleteIcon />
                        </IconButton>
                        <IconButton aria-label="edit" color="primary" disabled>
                            <EditIcon />
                        </IconButton>
                    </CardActions>
                }

            </Card>
        </>
    );
}

export default RatingCard;