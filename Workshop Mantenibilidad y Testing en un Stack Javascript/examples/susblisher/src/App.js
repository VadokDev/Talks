import ManageMessages from './layouts/ManageMessages';
import Read from './organisms/Read';
import Publish from './organisms/Publish';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { messageRepository } from './repositories';
import { Container } from '@mui/system';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container>
        <ManageMessages
          ReadOrganism={Read}
          PublishOrganism={Publish}
          messageRepository={messageRepository}
        ></ManageMessages>
      </Container>
    </ThemeProvider>
  );
}

export default App;
