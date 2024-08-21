```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.GetAllBrands
{
    [Route("api/organizations/{organizationId}/brands")]
    [ApiController]
    [ApiExplorerSettings(GroupName = "Brands")]
    public class GetAllBrandsController : Controller
    {
        /// <summary>
        /// Retrieves all Brands in the Organization tenant after an authorized client request.
        /// </summary>
        /// <param name="organizationId"></param>
        /// <param name="request"></param>
        /// <param name="mediator"></param>
        /// <returns></returns>
        [HttpGet]
        [Authorize]
        [ProducesResponseType(typeof(PaginatedResponse<GetAllBrandsDto>), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        [ProducesResponseType(StatusCodes.Status401Unauthorized)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [ProducesResponseType(StatusCodes.Status503ServiceUnavailable)]
        public async Task<IActionResult> GetAllBrands(
            [FromRoute] string organizationId, 
            [FromQuery] GetAllBrandsRequest request,
            [FromServices] IMediator mediator)
        {
            var query = new GetAllBrandsQuery(
                request.BrandIdOrName,
                request.BrandIds,
                request.OrderBy,
                request.OrderByDescending,
                request.Offset,
                request.Limit);

            var response = await mediator.Send(query);

            return Ok(response);
        }
    }
}
```