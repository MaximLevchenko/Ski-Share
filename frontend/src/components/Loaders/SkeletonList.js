import ContentLoader from "react-content-loader"


const SkeletonList = (props) => (
  <ContentLoader 
    speed={2}
    width={400}
    height={250}
    viewBox="0 0 400 250"
    backgroundColor="#f3f3f3"
    foregroundColor="#ecebeb"
    {...props}
  >
    <rect x="25" y="6" rx="5" ry="5" width="220" height="36" /> 
    <rect x="25" y="56" rx="5" ry="5" width="220" height="36" /> 
    <rect x="25" y="104" rx="5" ry="5" width="220" height="36" /> 
    <rect x="26" y="156" rx="5" ry="5" width="220" height="36" />
  </ContentLoader>
)

export default SkeletonList
