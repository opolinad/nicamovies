import React from 'react';
import CardContainer from './components/MoviesContainer';
import MovieDetail from './components/MovieDetail';
import Navbar from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import LogIn from './components/LogIn';
import SignUp from './components/SignUp';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path='/' element={ <CardContainer /> } />
        <Route path='/movie/:movieId' element={ <MovieDetail /> } />
        <Route path='/login' element={ <LogIn /> } />
        <Route path='/signup' element={ <SignUp /> } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
