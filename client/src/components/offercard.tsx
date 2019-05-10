import * as React from "react"
import styled from "styled-components"

const ExternalLink = styled.a`
  text-decoration: none;
  display: flex;
  margin-top: 1rem;
  grid-column: -2;
  background: #000099;
  color: #e6e6ff;
  font-family: helvetica;
  font-size: 0.8rem;
  align-items: center;
  justify-content: center;
  border-radius: 0.2rem;
  border: #00004d solid 0.1em;

  opacity: 0.9;
  &: hover {
    opacity: 1;
  }
`

const Card = styled.li`
  margin: 0;
  display: grid;
  background: #dfdfea;
  min-height: 8vw;
  width: 100%;
  padding: 1rem;
  grid-template-columns: 10px repeat(3, 1fr);
`

const CardTitle = styled.h4`
  grid-column: 1 / -1;
  margin-bottom: 0.5rem;
`

const Company = styled.i`
  grid-column: 2 / -1;
`

const Location = styled.span`
  grid-column: 2 / -1;
`

const OfferCard = ({ title, link, location, company }) => {
  return (
    <Card>
      <CardTitle>{title}</CardTitle>
      <Company>{company}</Company>
      <Location>{location}</Location>
      <ExternalLink href={link}>Visit URL</ExternalLink>
    </Card>
  )
}

export default OfferCard
