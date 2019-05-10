import * as React from "react"
import { Link, useStaticQuery, graphql } from "gatsby"
import styled from "styled-components"
import OfferCard from "./offercard"

const Grid = styled.ul`
  display: grid;
  grid-gap: 10px;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
`

const OfferOverview = () => {
  const { server } = useStaticQuery(
    graphql`
      query {
        server {
          offers {
            title
            link
            location
            company
          }
        }
      }
    `
  )
  return (
    <Grid>
      {server &&
        server.offers &&
        server.offers.map(o => <OfferCard key={o.link} {...o} />)}
    </Grid>
  )
}

export default OfferOverview
