import ManageMessages from './layouts/ManageMessages';
import { messageRepository } from './repositories';
import { Container } from '@mui/system';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container sx={{ pt: 5 }}>
        <ManageMessages messageRepository={messageRepository}></ManageMessages>
      </Container>
    </ThemeProvider>
  );
}

export default App;
