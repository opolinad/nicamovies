import React, { useEffect } from 'react';
import CardContainer from './components/MoviesContainer';
import Navbar from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path='/' element={ <CardContainer /> } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
