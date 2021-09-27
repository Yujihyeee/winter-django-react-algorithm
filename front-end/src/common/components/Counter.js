import { Badge } from '@mui/material'
import React, {useState} from 'react'
import MailIcon from '@mui/icons-material/Mail';


export default function Counter () {
    return(<div>
            <Badge badgeContent={4} color="secondary">
                <MailIcon color="action"/>
            </Badge>
            <button variant= "outlined">
                Add
            </button>
        </div>)
}
