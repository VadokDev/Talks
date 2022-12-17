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

const availableMessages = [
  { content: 'Workshop' },
  { content: 'Walmart' },
  { content: 'Este es el lugar' },
];

function App() {
  const [messages, setMessages] = useState([]);

  const readMessages = () => {
    axios
      .get('http://localhost:8000/messages')
      .then(({ data }) => setMessages(data));
  };

  const sendMessage = (content) => {
    const message = { content };
    axios
      .post('http://localhost:8000/messages', message)
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
                {availableMessages.map((message) => (
                  <Button
                    onClick={() => sendMessage(message.content)}
                    variant='outlined'
                  >
                    {message.content}
                  </Button>
                ))}
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
