import { Alert, Button, Rating, Snackbar, TextField, Typography } from '@mui/material';
import { useState } from 'react';
import { useParams } from 'react-router-dom';

const RatingForm = ({ fetchMovie }) => {
    const [value, setValue] = useState();
    const [comment, setComment] = useState('');
    const [alert, setAlert] = useState(null);
    const [open, setOpen] = useState(false);

    const { movieId } = useParams();
    const userId = localStorage.getItem('userId');

    const handleClose = (event = null, reason) => {
        if (reason === 'clickaway') {
          return;
        }
        setOpen(false);
    };

    const saveRating = () => {
        const params = {
            rating: value,
            comment: comment,
            Authorization: `Bearer ${localStorage.getItem('token')}`
        };
        const options = {
            method: 'POST',
            body: JSON.stringify(params),
        };
        fetch(`http://${process.env.REACT_APP_API_URL}/movie/${movieId}/user/${userId}/create-rating`, options )
            .then( response => response.json() )
            .then( response => {
                if (response.status) {
                    setAlert({
                        severity: 'success',
                        message: response.message
                    });
                    setOpen(true);
                    setValue(0);
                    setComment('');
                    fetchMovie();
                } else {
                    setAlert({
                        severity: 'error',
                        message: response.message
                    });
                    setOpen(true);
                }
            });
    }

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
            <Typography component="legend" sx={{ fontSize: '1.2rem', fontWeight: 'bolder', marginBottom: '5px' }}>Rating:</Typography>
            <Rating
                name="simple-controlled"
                value={value}
                onChange={(event, newValue) => {
                    setValue(newValue);
                }}
            />
            <Typography component="legend" sx={{ fontSize: '1.2rem', fontWeight: 'bolder', margin: '5px 0' }}>Comment:</Typography>
            <TextField
                placeholder="Place your thoughts of the movie"
                multiline
                rows={2}
                maxRows={4}
                fullWidth
                value={comment}
                onChange={event => setComment(event.target.value)}
            />
            <Button
                variant="contained"
                sx={{ marginTop: '15px', fontWeight: 'bolder', fontSize: '1rem' }}
                fullWidth
                onClick={saveRating}
            >
                Save
            </Button>

        </>
    );
}

export default RatingForm;