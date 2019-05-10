import * as React from "react"
import * as PropTypes from "prop-types"
import { Link, useStaticQuery, graphql } from "gatsby"

const OfferOverview = () => {
  const { server } = useStaticQuery(
    graphql`
      query {
        server {
          offers {
            title
            link
          }
        }
      }
    `
  )
  return (
    <ul>
      {server &&
        server.offers &&
        server.offers.map(o => <li key={o.link}>{o.title}</li>)}
    </ul>
  )
}

export default OfferOverview
