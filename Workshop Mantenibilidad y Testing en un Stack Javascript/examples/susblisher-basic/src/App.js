import { useState } from 'react';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import logo from './logo.png';
import axios from 'axios';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function App() {
  const [messages, setMessages] = useState([]);

  const readMessages = () => {
    axios
      .get('http://localhost:8000/messages')
      .then(({ data }) => setMessages(data));
  };

  const sendMessage = (content) => {
    const mensaje = { content };
    axios
      .post('http://localhost:8000/messages', mensaje)
      .then(() => readMessages());
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container sx={{ pt: 5 }}>
        <Grid container direction='column' alignItems={'center'}>
          <Grid item pb={5}>
            <img src={logo} alt='Walmart Chile'></img>
          </Grid>
          <Grid container spacing={2}>
            <Grid item xs={6}>
              <Stack spacing={2}>
                <Button
                  onClick={() => sendMessage('Workshop')}
                  variant='outlined'
                >
                  Workshop
                </Button>
                <Button
                  onClick={() => sendMessage('Walmart')}
                  variant='outlined'
                >
                  Walmart
                </Button>
                <Button
                  onClick={() => sendMessage('Este es el lugar')}
                  variant='outlined'
                >
                  Este es el lugar
                </Button>
              </Stack>
            </Grid>
            <Grid item xs={6}>
              <Grid alignContent={'center'}>
                <Box textAlign='center'>
                  <Button
                    variant='contained'
                    onClick={() => readMessages()}
                    sx={{ mb: 2 }}
                  >
                    Leer Mensajes
                  </Button>
                </Box>
                <Grid item>
                  <Stack spacing={2}>
                    {messages.map((message, i) => (
                      <Button key={`published-message-${i}`} variant='outlined'>
                        {message.content}
                      </Button>
                    ))}
                  </Stack>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

export default App;
