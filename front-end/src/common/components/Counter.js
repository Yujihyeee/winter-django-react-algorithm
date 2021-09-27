import { Badge } from '@mui/material'
import React, {useState} from 'react'
import MailIcon from '@mui/icons-material/Mail';
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import styled from 'styled-components'
import Button from '@mui/material/Button';



export default function Counter () {
    const [count, setCount] = useState(0)

    return(<Counterdiv>
            {count == 0 && <Stack sx={{ width: '300px', margin : '0 auto' }} spacing={2}>
                <Alert severity="error">
                    <AlertTitle>Error</AlertTitle>
                    메일이 없습니다.
                </Alert>
            </Stack>}
            <Badge badgeContent={count >= 0 ? count: setCount(0)} color="secondary" style={{marginBottom: '20px'}}>
                <MailIcon color="action"/>
            </Badge>
            <br/>
            <Button variant= "outlined" onClick={()=> setCount(count + 1)}>
                Add
            </Button>
            <SpanStyle/>
            <Button variant= "outlined" onClick={()=> setCount(count - 1)}>
                Del
            </Button>
        </Counterdiv>)
}

const Counterdiv = styled.div `text-align: center;`
const SpanStyle = styled.span `margin: 10px;`