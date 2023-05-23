import React from 'react';
import CardContainer from './components/MoviesContainer';
import MovieDetail from './components/MovieDetail';
import Navbar from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path='/' element={ <CardContainer /> } />
        <Route path='/movie/:movieId' element={ <MovieDetail /> } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
